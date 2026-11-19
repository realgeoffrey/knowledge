const test = require('node:test');
const assert = require('node:assert/strict');
const {existsSync, readFileSync} = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

test('多层抽屉逐层返回，保留父节点与焦点，复用为首层时恢复宽度', () => {
  const drawer = id => ({
    id, open: false, isConnected: true, input: {value: '未提交的输入'}, listeners: {},
    style: {values: {}, setProperty(key, value) { this.values[key] = value; }, removeProperty(key) { delete this.values[key]; }},
    addEventListener(name, callback) { this.listeners[name] = callback; },
    querySelector() { return this.body; }, body: {scrollTop: 0},
    getBoundingClientRect() { return {left: 500, right: 1000, top: 0, bottom: 800, width: 500}; },
    showModal() { this.open = true; }, close() { this.open = false; }, focus() { this.focused = true; }
  });
  const drawers = [drawer('parent'), drawer('child'), drawer('leaf')];
  const opener = drawer('opener');
  const document = {activeElement: opener, querySelectorAll: () => drawers};
  const context = {window: {addEventListener() {}}, document};
  const file = path.join(__dirname, '../../prototypes/interactive/assets/drawer.js');
  vm.runInNewContext(existsSync(file) ? readFileSync(file, 'utf8') : '', context);
  const layers = context.window.DrawerLayers;
  assert.equal(typeof layers?.open, 'function');
  const [parent, child, leaf] = drawers;
  const input = parent.input;
  layers.open(parent);
  document.activeElement = parent;
  parent.body.scrollTop = 168;
  layers.open(child);
  document.activeElement = child;
  layers.open(leaf);
  assert(drawers.every(modal => modal.open));
  assert.equal(child.style.values['--drawer-parent-width'], '500px');
  assert.equal(leaf.style.values['--drawer-parent-width'], '500px');
  layers.close(parent);
  assert.equal(parent.open, true);
  let prevented = false;
  leaf.listeners.cancel({preventDefault() { prevented = true; }});
  assert.equal(prevented, true);
  assert.equal(leaf.open, false);
  assert.equal(child.open, true);
  assert.equal(child.focused, true);
  child.listeners.click({target: child, clientX: 2, clientY: 200});
  assert.equal(child.open, false);
  assert.equal(parent.open, true);
  assert.equal(parent.input, input);
  assert.equal(input.value, '未提交的输入');
  assert.equal(parent.body.scrollTop, 168);
  assert.equal(parent.focused, true);
  layers.closeAll();
  assert.equal(parent.open, false);
  assert.equal(opener.focused, true);
  document.activeElement = opener;
  layers.open(child);
  assert.equal(child.style.values['--drawer-parent-width'], undefined);
  child.listeners.close();
  layers.open(leaf);
  leaf.close();
  child.listeners.cancel({preventDefault() {}});
  assert.equal(child.open, false);
  leaf.listeners.close();
  layers.closeAll();
  assert(drawers.every(modal => !modal.open));
});
