// Custom JavaScript for the tag widget
document.addEventListener('DOMContentLoaded', function() {
    const tagInput = document.querySelector('.tag-widget');
    if (tagInput) {
        tagInput.addEventListener('input', function(event) {
            console.log('Tag input changed:', event.target.value);
        });
    }
});