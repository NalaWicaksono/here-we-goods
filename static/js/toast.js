function showToast(title, message, type='info', duration=1800){
  const el = document.getElementById('toast-component');
  const t  = document.getElementById('toast-title');
  const m  = document.getElementById('toast-message');
  if(!el) return;

  // reset warna
  el.classList.remove('bg-violet-700','border-violet-500','bg-rose-700','border-rose-500','bg-slate-800','border-slate-700');

  if (type === 'success') {
    el.classList.add('bg-violet-700','border-violet-500');
  } else if (type === 'error') {
    el.classList.add('bg-rose-700','border-rose-500');
  } else {
    el.classList.add('bg-slate-800','border-slate-700');
  }

  t.textContent = title || '';
  m.textContent = message || '';

  el.classList.remove('opacity-0','translate-y-10');
  el.classList.add('opacity-100','translate-y-0');

  window.clearTimeout(el.__hideTimer);
  el.__hideTimer = window.setTimeout(()=>{
    el.classList.remove('opacity-100','translate-y-0');
    el.classList.add('opacity-0','translate-y-10');
  }, duration);
}
