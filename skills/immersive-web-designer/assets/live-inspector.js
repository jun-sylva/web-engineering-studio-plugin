(() => {
  if (window.ImmersiveWebDesignerLive?.active) return window.ImmersiveWebDesignerLive;

  const state = { active: true, hovered: null, selected: null };
  const host = document.createElement('div');
  host.id = 'iwd-live-inspector';
  host.style.cssText = 'position:fixed;inset:0;z-index:2147483647;pointer-events:none;font:12px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;color:#fff';
  const shadow = host.attachShadow({ mode: 'open' });
  shadow.innerHTML = `<style>
    :host{{all:initial}} .box{{position:fixed;border:2px solid #ffcc33;background:rgba(255,204,51,.08);pointer-events:none;transition:all 60ms linear}}
    .tag{{position:fixed;max-width:min(520px,calc(100vw - 24px));padding:7px 9px;background:#151513;color:#fff;border:1px solid #ffcc33;border-radius:4px;box-shadow:0 5px 30px #0008;pointer-events:none;white-space:pre-wrap}}
    .bar{{position:fixed;right:12px;bottom:12px;padding:8px 10px;background:#151513;color:#fff;border:1px solid #555;border-radius:6px;pointer-events:auto}}
    button{{font:inherit;color:#111;background:#ffcc33;border:0;border-radius:3px;padding:3px 7px;margin-left:8px;cursor:pointer}}
  </style><div class="box"></div><div class="tag"></div><div class="bar">IWD Live · click to inspect · Esc to stop <button>Stop</button></div>`;
  document.documentElement.appendChild(host);
  const box = shadow.querySelector('.box');
  const tag = shadow.querySelector('.tag');

  function selectorFor(element) {
    if (element.id) return `#${CSS.escape(element.id)}`;
    const parts = [];
    let current = element;
    while (current && current.nodeType === Node.ELEMENT_NODE && parts.length < 6) {
      let part = current.localName;
      const stableClasses = [...current.classList].filter((name) => !/^(active|selected|hover|focus|open|css-|jsx-)/.test(name)).slice(0, 2);
      if (stableClasses.length) part += stableClasses.map((name) => `.${CSS.escape(name)}`).join('');
      const siblings = current.parentElement ? [...current.parentElement.children].filter((node) => node.localName === current.localName) : [];
      if (siblings.length > 1) part += `:nth-of-type(${siblings.indexOf(current) + 1})`;
      parts.unshift(part); current = current.parentElement;
    }
    return parts.join(' > ');
  }

  function accessibleName(element) {
    return element.getAttribute('aria-label') || element.getAttribute('alt') || element.getAttribute('title') || element.labels?.[0]?.textContent?.trim() || element.textContent?.trim().replace(/\s+/g, ' ').slice(0, 120) || '';
  }

  function describe(element) {
    const rect = element.getBoundingClientRect();
    const style = getComputedStyle(element);
    return {
      selector: selectorFor(element), tag: element.localName, role: element.getAttribute('role') || '', name: accessibleName(element),
      rect: { x: Math.round(rect.x), y: Math.round(rect.y), width: Math.round(rect.width), height: Math.round(rect.height) },
      style: { display: style.display, position: style.position, color: style.color, backgroundColor: style.backgroundColor, font: style.font, borderRadius: style.borderRadius, zIndex: style.zIndex },
      viewport: { width: innerWidth, height: innerHeight, dpr: devicePixelRatio }, url: location.href
    };
  }

  function place(element) {
    if (!element || element === host || host.contains(element)) return;
    state.hovered = element;
    const rect = element.getBoundingClientRect();
    Object.assign(box.style, { left:`${rect.left}px`, top:`${rect.top}px`, width:`${rect.width}px`, height:`${rect.height}px` });
    const label = `${element.localName}${element.id ? `#${element.id}` : ''}  ${Math.round(rect.width)}×${Math.round(rect.height)}`;
    tag.textContent = label;
    const top = rect.top > 42 ? rect.top - 34 : Math.min(innerHeight - 36, rect.bottom + 4);
    Object.assign(tag.style, { left:`${Math.max(6, Math.min(rect.left, innerWidth - 320))}px`, top:`${top}px` });
  }

  function onMove(event) { place(event.target); }
  function onClick(event) {
    if (event.composedPath().includes(host)) return;
    event.preventDefault(); event.stopPropagation();
    state.selected = describe(event.target);
    window.__IWD_SELECTION__ = state.selected;
    console.info('IWD_SELECTION', JSON.stringify(state.selected));
    tag.textContent = `Selected: ${state.selected.selector}\nDetails: window.__IWD_SELECTION__`;
  }
  function stop() {
    if (!state.active) return;
    state.active = false;
    document.removeEventListener('pointermove', onMove, true);
    document.removeEventListener('click', onClick, true);
    document.removeEventListener('keydown', onKey, true);
    host.remove();
  }
  function onKey(event) { if (event.key === 'Escape') stop(); }
  shadow.querySelector('button').addEventListener('click', stop);
  document.addEventListener('pointermove', onMove, true);
  document.addEventListener('click', onClick, true);
  document.addEventListener('keydown', onKey, true);
  window.ImmersiveWebDesignerLive = { ...state, stop, describe, selectorFor, get selection() { return state.selected; }, active: true };
  console.info('IWD Live inspector started. Click an element; read window.__IWD_SELECTION__. Press Escape to stop.');
  return window.ImmersiveWebDesignerLive;
})();
