
(function ($) {

  "use strict";

  // COUNTER NUMBERS
  jQuery('.counter-thumb').appear(function () {
    jQuery('.counter-number').countTo();
  });

  // CUSTOM LINK
  $('.smoothscroll').click(function () {
    var el = $(this).attr('href');
    var elWrapped = $(el);
    var header_height = $('.navbar').height();

    scrollToDiv(elWrapped, header_height);
    return false;

    function scrollToDiv(element, navheight) {
      var offset = element.offset();
      var offsetTop = offset.top;
      var totalScroll = offsetTop - navheight;

      $('body,html').animate({
        scrollTop: totalScroll
      }, 300);
    }
  });

  // Get references to the select element and the additional options div
  const serviceTypeSelect = document.getElementById("service-type");
  const combinacionOptions = document.getElementById("combinacion-options");
  const transporteOptions = document.getElementById("transporte-options");
  const almacenamientoOptions = document.getElementById("almacenamiento-options");




  // Add an event listener to the select element
  serviceTypeSelect.addEventListener("change", function () {
    if (serviceTypeSelect.value === "Combinación de servicios") {
      // If "Combinación de servicios" is selected, show the additional options
      combinacionOptions.style.display = "block";
      almacenamientoOptions.style.display = "none";


    } else if (serviceTypeSelect.value === "Transporte" || serviceTypeSelect.value === "Distribución") {
      transporteOptions.style.display = "block";
      combinacionOptions.style.display = "none";
      almacenamientoOptions.style.display = "none";


    }
    else {
      // Otherwise, hide the additional options
      combinacionOptions.style.display = "none";
      transporteOptions.style.display = "none";
      almacenamientoOptions.style.display = "block";
    }
  });


  // Get references to the checkboxes
  const service1Checkbox = document.getElementById("service1");
  const service2Checkbox = document.getElementById("service2");
  const service3Checkbox = document.getElementById("service3");

  // Add event listeners to the checkboxes
  service1Checkbox.addEventListener("change", handleCheckboxChange);
  service2Checkbox.addEventListener("change", handleCheckboxChange);
  service3Checkbox.addEventListener("change", handleCheckboxChange);

  // Function to handle checkbox changes
  function handleCheckboxChange() {
    const isService1Checked = service1Checkbox.checked;
    const isService2Checked = service2Checkbox.checked;
    const isService3Checked = service3Checkbox.checked;

    if ((isService1Checked || isService3Checked) && !isService2Checked) {
      // If only service2 is checked, hide transporteOptions
      transporteOptions.style.display = "block";
      almacenamientoOptions.style.display = "none";

    } else if (isService1Checked && isService2Checked || isService3Checked && isService2Checked) {
      // For all other cases, show transporteOptions
      almacenamientoOptions.style.display = "block";
      transporteOptions.style.display = "block";
    }
    else {
      transporteOptions.style.display = "none";
      almacenamientoOptions.style.display = "block";
    }
  };


  const rfcbox = document.getElementById("rfcbox");
  const facturaSiRadio = document.getElementById("facturaSi");
  const facturaNoRadio = document.getElementById("facturaNo");

  function handleRadioChange() {
    if (facturaSiRadio.checked) {
      rfcbox.style.display = "block";
    } else {
      rfcbox.style.display = "none";
    }
  }

  facturaSiRadio.addEventListener("change", handleRadioChange);
  facturaNoRadio.addEventListener("change", handleRadioChange);

  // Initialize the display based on the initial state of radio buttons
  handleRadioChange();


  $(document).ready(function () {
    // Capture form submission event
    $("#myForm").submit(function (event) {
      var volumen = $("#volumen").val(); // Get the value of the name field
      var precio_factura = $("#precio_factura").val(); // Get the value of the email field

      // Check if the name field is empty
      if (volumen === "") {
        alert("El volumen es necesario.");
        event.preventDefault(); // Prevent form submission
        return;
      }
      if (precio_factura === "") {
        alert("Please enter your name.");
        event.preventDefault(); // Prevent form submission
        return;
      }


      // If all fields are filled, continue with form submission
    });
  });


})(window.jQuery);

