document.addEventListener('DOMContentLoaded', function() {
  const div = document.querySelectorAll('.categroup');
  
  div.forEach(function(d) {
    d.addEventListener('mouseover', function() {
      d.style.transform = 'scale(1.2)';
    });
      
    d.addEventListener('mouseout', function() {
      d.style.transform = 'scale(1)';
    });
  });
});