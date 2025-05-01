---
layout: page
title: Notice Period
---
<style type="text/css" media="screen">
  .container {
    margin: 30px auto;
    max-width: 600px;
    text-align: center;
  }
    #countdown {
        padding-top: 20px;
        font-size: 200px;
    }
</style>
<div class="container">
    <div id="countdown"></div>
    <h3>days left only</h3>
    <script>
        function calculateDaysLeft() {
            const lastWorkingDay = new Date("July 22, 2025");
            const today = new Date();
            const timeDiff = lastWorkingDay - today;
            const daysLeft = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
            return daysLeft;
        }


        document.getElementById("countdown").innerText = `${calculateDaysLeft()}`;
    </script>
</div>