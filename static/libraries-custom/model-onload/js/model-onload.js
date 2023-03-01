var profileMissingModal = new bootstrap.Modal(
  document.getElementById("profileMissingModal"),
  {}
);
document.onreadystatechange = function () {
  profileMissingModal.show();
};
