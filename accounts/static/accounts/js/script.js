$(document).ready(function () {
  // Cache jQuery selectors
  var overlay = $(".overlay"),
    hiveTab = $("#hiveCreation"),
    hivedelete = $("#hivedelete"),
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
    hivedelete.hide()
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

  
  $("#hive_delete").click(function () {
    showOverlayAndElement(hivedelete);
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
