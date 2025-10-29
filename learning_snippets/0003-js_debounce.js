// Mini: debounce utility (ES module)
// Usage (browser/node with ESM):
// const debounced = debounce(fn, 200);
// debounced();

export function debounce(fn, wait = 200) {
  let t = null;
  return function (...args) {
    if (t) clearTimeout(t);
    t = setTimeout(() => fn.apply(this, args), wait);
  };
}

// quick example (uncomment to test in browser):
// const log = (x) => console.log('called', x);
// const d = debounce(log, 100);
// d(1); d(2); d(3);
