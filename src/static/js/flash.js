document.addEventListener('DOMContentLoaded', () => {
  const alerts = document.querySelectorAll('.alert');
  if (!alerts.length) return;

  alerts.forEach(alert => {
    // Dismiss after 3 seconds
    const timeout = setTimeout(() => {
      alert.classList.add('hide');
    }, 3000);

    // Allow manual dismissal on click (optional)
    alert.addEventListener('click', () => {
      clearTimeout(timeout);
      alert.classList.add('hide');
    });

    // Remove from DOM after transition finishes
    alert.addEventListener('transitionend', (e) => {
      // Ensure we react to opacity/transform transition end
      if (e.propertyName === 'opacity' || e.propertyName === 'transform') {
        if (alert.parentNode) alert.parentNode.removeChild(alert);
      }
    }, { once: true });
  });
});
