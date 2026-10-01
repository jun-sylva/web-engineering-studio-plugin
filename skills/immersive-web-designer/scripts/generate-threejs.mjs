#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";

const args = process.argv.slice(2);
const force = args.includes("--force");
const positional = args.filter((arg) => arg !== "--force");

if (positional.length !== 2) {
  console.error("Usage: generate-threejs.mjs <spec.json> <output.js> [--force]");
  process.exit(2);
}

const [specPath, outputPath] = positional.map((value) => path.resolve(value));

if (!fs.existsSync(specPath)) {
  console.error(`Specification not found: ${specPath}`);
  process.exit(2);
}
if (fs.existsSync(outputPath) && !force) {
  console.error(`Refusing to overwrite ${outputPath}; pass --force after reviewing the existing file.`);
  process.exit(2);
}

let spec;
try {
  spec = JSON.parse(fs.readFileSync(specPath, "utf8"));
} catch (error) {
  console.error(`Invalid JSON specification: ${error.message}`);
  process.exit(2);
}

const geometryTypes = new Set(["box", "sphere", "cylinder", "cone", "torus", "capsule", "plane", "ring", "lathe", "extrude", "tube"]);
const materialTypes = new Set(["standard", "physical", "basic", "lambert", "phong", "normal"]);
const lightTypes = new Set(["ambient", "hemisphere", "directional", "point", "spot"]);

function finiteNumber(value, location) {
  if (typeof value !== "number" || !Number.isFinite(value)) throw new Error(`${location} must be a finite number`);
}

function tuple(value, length, location) {
  if (!Array.isArray(value) || value.length !== length) throw new Error(`${location} must contain ${length} numbers`);
  value.forEach((item, index) => finiteNumber(item, `${location}[${index}]`));
}

function validateNode(node, location, materialNames) {
  if (!node || typeof node !== "object" || Array.isArray(node)) throw new Error(`${location} must be an object`);
  if (typeof node.name !== "string" || !node.name.trim()) throw new Error(`${location}.name is required`);
  if (node.position) tuple(node.position, 3, `${location}.position`);
  if (node.rotation) tuple(node.rotation, 3, `${location}.rotation`);
  if (node.scale) tuple(node.scale, 3, `${location}.scale`);
  if (node.geometry) {
    if (!geometryTypes.has(node.geometry.type)) throw new Error(`${location}.geometry.type is unsupported: ${node.geometry.type}`);
    if (node.geometry.type === "lathe") {
      if (!Array.isArray(node.geometry.points) || node.geometry.points.length < 2) throw new Error(`${location}.geometry.points needs at least two [radius,y] points`);
      node.geometry.points.forEach((point, index) => tuple(point, 2, `${location}.geometry.points[${index}]`));
    }
    if (node.geometry.type === "extrude") {
      if (!Array.isArray(node.geometry.shape) || node.geometry.shape.length < 3) throw new Error(`${location}.geometry.shape needs at least three [x,y] points`);
      node.geometry.shape.forEach((point, index) => tuple(point, 2, `${location}.geometry.shape[${index}]`));
    }
    if (node.geometry.type === "tube") {
      if (!Array.isArray(node.geometry.points) || node.geometry.points.length < 2) throw new Error(`${location}.geometry.points needs at least two [x,y,z] points`);
      node.geometry.points.forEach((point, index) => tuple(point, 3, `${location}.geometry.points[${index}]`));
    }
    if (typeof node.material !== "string" || !materialNames.has(node.material)) throw new Error(`${location}.material must reference a declared material`);
  }
  if (node.children) {
    if (!Array.isArray(node.children)) throw new Error(`${location}.children must be an array`);
    node.children.forEach((child, index) => validateNode(child, `${location}.children[${index}]`, materialNames));
  }
}

try {
  if (!spec || typeof spec !== "object" || Array.isArray(spec)) throw new Error("root must be an object");
  if (!spec.materials || typeof spec.materials !== "object" || Array.isArray(spec.materials)) throw new Error("materials must be an object");
  const materialNames = new Set(Object.keys(spec.materials));
  for (const [name, material] of Object.entries(spec.materials)) {
    if (!material || typeof material !== "object" || !materialTypes.has(material.type)) throw new Error(`materials.${name}.type is unsupported`);
  }
  if (!Array.isArray(spec.nodes) || spec.nodes.length === 0) throw new Error("nodes must contain at least one node");
  spec.nodes.forEach((node, index) => validateNode(node, `nodes[${index}]`, materialNames));
  if (spec.camera?.position) tuple(spec.camera.position, 3, "camera.position");
  if (spec.camera?.target) tuple(spec.camera.target, 3, "camera.target");
  if (spec.lights) {
    if (!Array.isArray(spec.lights)) throw new Error("lights must be an array");
    spec.lights.forEach((light, index) => {
      if (!lightTypes.has(light.type)) throw new Error(`lights[${index}].type is unsupported: ${light.type}`);
      if (light.position) tuple(light.position, 3, `lights[${index}].position`);
      if (light.target) tuple(light.target, 3, `lights[${index}].target`);
    });
  }
} catch (error) {
  console.error(`Specification validation failed: ${error.message}`);
  process.exit(2);
}

const serialized = JSON.stringify(spec, null, 2).replaceAll("</script", "<\\/script");
const generated = `// Generated by immersive-web-designer from ${path.basename(specPath)}.
// Edit the JSON specification and regenerate instead of scattering shape constants here.
import * as THREE from "three";

export const PROCEDURAL_SPEC = ${serialized};

function vector3(value, fallback) {
  const source = value ?? fallback;
  return new THREE.Vector3(source[0], source[1], source[2]);
}

function geometryFrom(definition) {
  const d = definition;
  switch (d.type) {
    case "box": return new THREE.BoxGeometry(...(d.size ?? [1, 1, 1]), ...(d.segments ?? [1, 1, 1]));
    case "sphere": return new THREE.SphereGeometry(d.radius ?? 1, d.widthSegments ?? 32, d.heightSegments ?? 20);
    case "cylinder": return new THREE.CylinderGeometry(d.radiusTop ?? 1, d.radiusBottom ?? 1, d.height ?? 1, d.radialSegments ?? 32, d.heightSegments ?? 1, d.openEnded ?? false);
    case "cone": return new THREE.ConeGeometry(d.radius ?? 1, d.height ?? 1, d.radialSegments ?? 32, d.heightSegments ?? 1, d.openEnded ?? false);
    case "torus": return new THREE.TorusGeometry(d.radius ?? 1, d.tube ?? 0.25, d.radialSegments ?? 16, d.tubularSegments ?? 64, d.arc ?? Math.PI * 2);
    case "capsule": return new THREE.CapsuleGeometry(d.radius ?? 0.5, d.length ?? 1, d.capSegments ?? 8, d.radialSegments ?? 16);
    case "plane": return new THREE.PlaneGeometry(...(d.size ?? [1, 1]), ...(d.segments ?? [1, 1]));
    case "ring": return new THREE.RingGeometry(d.innerRadius ?? 0.5, d.outerRadius ?? 1, d.thetaSegments ?? 32, d.phiSegments ?? 1, d.thetaStart ?? 0, d.thetaLength ?? Math.PI * 2);
    case "lathe": return new THREE.LatheGeometry(d.points.map(([x, y]) => new THREE.Vector2(x, y)), d.segments ?? 32, d.phiStart ?? 0, d.phiLength ?? Math.PI * 2);
    case "extrude": {
      const shape = new THREE.Shape();
      d.shape.forEach(([x, y], index) => index === 0 ? shape.moveTo(x, y) : shape.lineTo(x, y));
      shape.closePath();
      return new THREE.ExtrudeGeometry(shape, { depth: d.depth ?? 0.25, bevelEnabled: d.bevelEnabled ?? true, bevelThickness: d.bevelThickness ?? 0.05, bevelSize: d.bevelSize ?? 0.04, bevelSegments: d.bevelSegments ?? 2, steps: d.steps ?? 1 });
    }
    case "tube": {
      const curve = new THREE.CatmullRomCurve3(d.points.map((point) => vector3(point, [0, 0, 0])), d.closed ?? false, d.curveType ?? "centripetal", d.tension ?? 0.5);
      return new THREE.TubeGeometry(curve, d.tubularSegments ?? 64, d.radius ?? 0.1, d.radialSegments ?? 12, d.closed ?? false);
    }
    default: throw new Error(\`Unsupported geometry: \${d.type}\`);
  }
}

function materialFrom(definition) {
  const { type, ...parameters } = definition;
  const constructors = {
    standard: THREE.MeshStandardMaterial,
    physical: THREE.MeshPhysicalMaterial,
    basic: THREE.MeshBasicMaterial,
    lambert: THREE.MeshLambertMaterial,
    phong: THREE.MeshPhongMaterial,
    normal: THREE.MeshNormalMaterial,
  };
  return new constructors[type](parameters);
}

function applyTransform(object, definition) {
  object.position.copy(vector3(definition.position, [0, 0, 0]));
  object.rotation.set(...(definition.rotation ?? [0, 0, 0]));
  object.scale.copy(vector3(definition.scale, [1, 1, 1]));
}

function nodeFrom(definition, materials) {
  const object = definition.geometry
    ? new THREE.Mesh(geometryFrom(definition.geometry), materials.get(definition.material))
    : new THREE.Group();
  object.name = definition.name;
  object.castShadow = definition.castShadow ?? false;
  object.receiveShadow = definition.receiveShadow ?? false;
  object.userData = { ...(definition.userData ?? {}), proceduralSource: true };
  applyTransform(object, definition);
  for (const child of definition.children ?? []) object.add(nodeFrom(child, materials));
  return object;
}

function lightFrom(definition) {
  let light;
  if (definition.type === "ambient") light = new THREE.AmbientLight(definition.color ?? 0xffffff, definition.intensity ?? 1);
  if (definition.type === "hemisphere") light = new THREE.HemisphereLight(definition.skyColor ?? 0xffffff, definition.groundColor ?? 0x444444, definition.intensity ?? 1);
  if (definition.type === "directional") light = new THREE.DirectionalLight(definition.color ?? 0xffffff, definition.intensity ?? 1);
  if (definition.type === "point") light = new THREE.PointLight(definition.color ?? 0xffffff, definition.intensity ?? 1, definition.distance ?? 0, definition.decay ?? 2);
  if (definition.type === "spot") light = new THREE.SpotLight(definition.color ?? 0xffffff, definition.intensity ?? 1, definition.distance ?? 0, definition.angle ?? Math.PI / 3, definition.penumbra ?? 0, definition.decay ?? 2);
  light.name = definition.name ?? \`\${definition.type}-light\`;
  light.position.copy(vector3(definition.position, [0, 0, 0]));
  light.castShadow = definition.castShadow ?? false;
  if (light.target && definition.target) light.target.position.copy(vector3(definition.target, [0, 0, 0]));
  return light;
}

export function createProceduralScene(options = {}) {
  const spec = options.spec ?? PROCEDURAL_SPEC;
  const scene = new THREE.Scene();
  if (spec.background) scene.background = new THREE.Color(spec.background);
  const materials = new Map(Object.entries(spec.materials).map(([name, definition]) => [name, materialFrom(definition)]));
  const root = new THREE.Group();
  root.name = spec.name ?? "procedural-model";
  for (const node of spec.nodes) root.add(nodeFrom(node, materials));
  scene.add(root);
  for (const lightDefinition of spec.lights ?? []) {
    const light = lightFrom(lightDefinition);
    scene.add(light);
    if (light.target && lightDefinition.target) scene.add(light.target);
  }
  const cameraDefinition = spec.camera ?? {};
  const camera = new THREE.PerspectiveCamera(cameraDefinition.fov ?? 35, 1, cameraDefinition.near ?? 0.01, cameraDefinition.far ?? 1000);
  camera.position.copy(vector3(cameraDefinition.position, [4, 3, 6]));
  camera.lookAt(vector3(cameraDefinition.target, [0, 0, 0]));
  const animations = spec.animations ?? [];
  function update(elapsedSeconds) {
    for (const animation of animations) {
      const target = root.getObjectByName(animation.target);
      if (!target) continue;
      const speed = animation.speed ?? 1;
      const amplitude = animation.amplitude ?? 1;
      if (animation.type === "spin") target.rotation[animation.axis ?? "y"] = elapsedSeconds * speed;
      if (animation.type === "float") target.position[animation.axis ?? "y"] = (animation.origin ?? 0) + Math.sin(elapsedSeconds * speed) * amplitude;
    }
  }
  function dispose() {
    root.traverse((object) => object.geometry?.dispose());
    for (const material of materials.values()) material.dispose();
  }
  return { scene, root, camera, materials, update, dispose };
}
`;

fs.mkdirSync(path.dirname(outputPath), { recursive: true });
fs.writeFileSync(outputPath, generated, "utf8");
console.log(`Generated ${outputPath}`);
