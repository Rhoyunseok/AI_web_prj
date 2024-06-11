window.addEventListener('DOMContentLoaded', function() {
  var mapContainer = document.getElementById('map');
  var mapFrame = document.createElement('iframe');
  mapFrame.src = '/map/whiskeymap/whiskeymap.html';
  mapFrame.width = '400';
  mapFrame.height = '300';
  mapFrame.frameborder = '0';
  mapFrame.style.border = '0';
  mapFrame.allowfullscreen = true;
  mapContainer.appendChild(mapFrame);
})