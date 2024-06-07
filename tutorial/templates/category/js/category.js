function toggleDropdown(id) {
  var dropdown = document.getElementById(id);
  if (dropdown.style.display === "none" || dropdown.style.display === "") {
    dropdown.style.display = "flex";
  }
  else {
    dropdown.style.display = "none";
  }
}