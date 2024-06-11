window.addEventListener('DOMContentLoaded', function() {
  var mapContainer = document.getElementById('map');
  var mapFrame = document.createElement('iframe');
  mapFrame.src = '/tutorial/map/winemap/wine.html';
  mapFrame.width = '600';
  mapFrame.height = '450';
  mapFrame.frameborder = '0';
  mapFrame.style.border = '0';
  mapFrame.allowfullscreen = true;
  mapContainer.appendChild(mapFrame);
})