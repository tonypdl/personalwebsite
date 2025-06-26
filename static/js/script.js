document.addEventListener('DOMContentLoaded', () => {
    const points = document.querySelectorAll('details.platform-point');
    points.forEach(point => {
        point.addEventListener('toggle', () => {
            if (point.open) {
                points.forEach(other => {
                    if (other !== point) {
                        other.removeAttribute('open');
                    }
                });
            }
        });
    });
});
