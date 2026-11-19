'use strict';

window.DrawerLayers = (() => {
  let stack = [];
  function resize() {
    stack.forEach(({modal}, index) => {
      if (index) modal.style.setProperty('--drawer-parent-width', stack[index - 1].modal.getBoundingClientRect().width + 'px');
      else modal.style.removeProperty('--drawer-parent-width');
    });
  }
  function forget(modal) {
    // Native close events are queued; this drawer may already have reopened.
    if (modal.open) return;
    const index = stack.findIndex(layer => layer.modal === modal);
    if (index < 0) return;
    const wasTop = index === stack.length - 1;
    const [layer] = stack.splice(index, 1);
    if (wasTop && layer.opener?.isConnected) layer.opener.focus({preventScroll: true});
  }
  function close(modal) {
    while (stack.length && !stack.at(-1).modal.open) forget(stack.at(-1).modal);
    modal ??= stack.at(-1)?.modal;
    if (!modal || modal !== stack.at(-1)?.modal) return;
    modal.close();
    forget(modal);
  }
  document.querySelectorAll('dialog.drawer').forEach(modal => {
    modal.addEventListener('close', () => forget(modal));
    modal.addEventListener('cancel', event => { event.preventDefault(); close(modal); });
    modal.addEventListener('click', event => {
      if (event.target !== modal) return;
      const {left, right, top, bottom} = modal.getBoundingClientRect();
      if (event.clientX < left || event.clientX > right || event.clientY < top || event.clientY > bottom) close(modal);
    });
  });
  window.addEventListener('resize', resize);
  return {
    open(modal) {
      if (modal.open) return;
      stack = stack.filter(layer => layer.modal.open);
      const opener = document.activeElement;
      modal.showModal();
      stack.push({modal, opener});
      resize();
      modal.querySelector('.drawer-body').scrollTop = 0;
    },
    close,
    closeAll() { while (stack.length) close(); }
  };
})();
