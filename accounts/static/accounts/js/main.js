$(document).ready(function () {
  $(".form")
    .find("input, textarea")
    .on("keyup blur focus", function (e) {
      var $this = $(this),
        label = $this.prev("label");

      if (e.type === "keyup") {
        if ($this.val() === "") {
          label.removeClass("active highlight");
        } else {
          label.addClass("active highlight");
        }
      } else if (e.type === "blur") {
        if ($this.val() === "") {
          label.removeClass("active highlight");
        } else {
          label.removeClass("highlight");
        }
      } else if (e.type === "focus") {
        if ($this.val() === "") {
          label.removeClass("highlight");
        } else if ($this.val() !== "") {
          label.addClass("highlight");
        }
      }
    });

  $(".tab a").on("click", function (e) {
    e.preventDefault();

    $(this).parent().addClass("active");
    $(this).parent().siblings().removeClass("active");

    target = $(this).attr("href");

    $(".tab-content > div").not(target).hide();

    $(target).fadeIn(600);
  });

  // Handle dropdown menus
  $(".navbar .dropdown-toggler").click(function (event) {
    event.preventDefault(); // Prevent default link behavior
    const targetDropdown = $(this).data("dropdown");
    const target = $(`#${targetDropdown}`);

    target.toggleClass("show");
  });

  // Close dropdowns when clicking outside
  $(window).mouseup(function (event) {
    if (!$(event.target).closest(".dropdown-toggler, .dropdown").length) {
      $(".navbar .dropdown").removeClass("show");
    }
  });

  // Handle small screens menu toggle
  $(".navbar-toggler").click(function (event) {
    event.preventDefault();
    $(".navbar-menu").toggleClass("active");
  });
});
