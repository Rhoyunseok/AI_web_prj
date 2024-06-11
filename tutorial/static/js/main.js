document.addEventListener('DOMContentLoaded', function() {
  const category = document.querySelectorAll('.categroup');
  
  category.forEach(function(categroup) {
    categroup.addEventListener('mouseover', function() {
      categroup.style.transform = 'scale(1.2)';
    });
      
    categroup.addEventListener('mouseout', function() {
      categroup.style.transform = 'scale(1)';
    });
  });
});