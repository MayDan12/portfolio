$(document).ready(function () {
  let login_btn = $("#login");
  let signup_btn = $("#signup");

  let signup = $("#sign_up");
  let signups = $("#sign_ups");

  let login_page = $("#login_page");
  let signup_page = $("#signup_page");

  signup_btn.click(function () {
    window.location.href = "login.html";
  });

  signup.click(function () {
    login_page.addClass("hidden");
    signup_page.addClass("visible");
  });

  signups.click(function () {
    login_page.addClass("hidden");
    signup_page.addClass("visible");
  });

  login_btn.click(function () {
    window.location.href = "login.html";
  });

  var $body = $("body");
  var $menuTrigger = $body.find(".menu-trigger");

  if ($menuTrigger.length) {
    $menuTrigger.click(function () {
      $body.toggleClass("menu-active");
    });
  }

  // Cache jQuery selectors
  var overlay = $(".overlay"),
    hiveTab = $("#hiveCreation"),
    hiveList = $("#hivelist"),
    taskTab = $("#taskCreation");

  // Function to show overlay and element
  function showOverlayAndElement(element) {
    overlay.show();
    element.show();
  }

  // Function to hide overlay and elements
  function hideOverlayAndElements() {
    overlay.hide();
    hiveTab.hide();
    hiveList.hide();
    taskTab.hide();
  }

  // Event handler for creating hive
  $("#create_hive").click(function () {
    showOverlayAndElement(hiveTab);
  });

  // Event handler for clicking on hive list
  $("#hivlist").click(function () {
    showOverlayAndElement(hiveList);
  });

  // Event handler for creating task
  $("#create_task").click(function () {
    showOverlayAndElement(taskTab);
  });

  // Event handler for overlay click
  overlay.click(function (event) {
    // Check if the click target is the overlay itself
    if ($(event.target).hasClass("overlay")) {
      hideOverlayAndElements();
    }
  });

  // Slider

  // Select buttons and feature list
  // const slideButtons = $(".contain .slide-button");
  // const featureList = $(".contain .flex-box");

  // // Add click event listener to buttons
  // slideButtons.click(function () {
  //   const buttonId = $(this).attr("id");
  //   const direction = buttonId === "prev-slide" ? -1 : 1;
  //   const scrollAmount = featureList.width() * direction;

  //   // Animate scroll with smooth behavior
  //   featureList.animate(
  //     {
  //       scrollLeft: scrollAmount,
  //     },
  //     "smooth"
  //   );
  // });

  // // Select slide buttons
  // const slideButtons = $(".contain .slide-button");
  // const feature_list = $(".contain .feature_box");

  // // Add click event listener
  // slideButtons.click(function () {
  //   this.click(function () {
  //     const direction = this.id === "prev-slide" ? -1 : 1;
  //     const scrollAmount = feature_list.clientWidth * direction;
  //     feature_list.scrollBy({ left: scrollAmount, behavior: "smooth" });
  //   });
  //   // console.log($(this));
  // });
});
