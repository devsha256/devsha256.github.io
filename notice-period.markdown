---
layout: default
title: Notice Period
# permalink: /notice-periods/
---

<style type="text/css" media="screen">
  .container {
    margin: 30px auto;
    max-width: 600px;
    text-align: center;
  }

  #countdown {
    font-size: 200px;
    cursor: pointer;
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    position: relative;
    opacity: 0;
    transform: translateY(-100vh);
    animation: dropIn 1s ease-out forwards;
  }

  /* Drop-in animation */
  @keyframes dropIn {
    0% { transform: translateY(-100vh); opacity: 0; }
    100% { transform: translateY(0); opacity: 1; }
  }

  /* Hover effect */
  #countdown:hover {
    text-shadow: 0px 0px 20px #000000;
    transform: scale(1.2);
    transition: 0.3s ease-in-out;
  }
</style>

<div class="container">
  <div id="countdown"></div>
  <h3>days left only</h3>
</div>

<script>
  function calculateDaysLeft() {
    const lastWorkingDay = new Date("July 22, 2025");
    const today = new Date();
    const timeDiff = lastWorkingDay - today;
    const daysLeft = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
    return daysLeft;
  }

  document.addEventListener("DOMContentLoaded", () => {
    const countdownElement = document.getElementById("countdown");
    countdownElement.textContent = calculateDaysLeft();
  });
</script>
