---
layout: default
title: Notice Period
permalink: /notice-period/
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

  @keyframes dropIn {
    0% { transform: translateY(-100vh); opacity: 0; }
    100% { transform: translateY(0); opacity: 1; }
  }

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

<div id="notice-period-root"></div>

<script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
<script crossorigin src="https://unpkg.com/axios/dist/axios.min.js"></script>

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

const { useState } = React;

function NoticeForm() {
  const [email, setEmail] = useState('');
  const [selectedDays, setSelectedDays] = useState(null);
  const [message, setMessage] = useState('');

  const dayOptions = [60, 45, 30, 15];

  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  const handleSubmit = async () => {
    if (!isValidEmail(email)) {
      setMessage('Please enter a valid email.');
      return;
    }
    if (!selectedDays) {
      setMessage('Please select a reminder time.');
      return;
    }

    const cronTime = calculateCron(selectedDays);

    const subscriber = { email, cron: cronTime };

    try {
      const res = await fetch('/.github/workflows/subscribers.yaml');
      const text = await res.text();
      if (text.includes(`- email: ${email}`) && text.includes(`cron: ${cronTime}`)) {
        setMessage('Warning: You are already subscribed. Update email or days.');
        return;
      }

      const updateResponse = await fetch('/.github/workflows/subscribe-action.yaml', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ subscriber })
      });

      if (updateResponse.ok) {
        setMessage('Successfully subscribed!');
      } else {
        setMessage('Error submitting request.');
      }
    } catch (error) {
      setMessage('Failed to process your subscription.');
    }
  };

  function calculateCron(daysBefore) {
    const noticeEnd = new Date();
    noticeEnd.setDate(noticeEnd.getDate() + daysBefore);
    const minute = noticeEnd.getMinutes();
    const hour = noticeEnd.getHours();
    const day = noticeEnd.getDate();
    const month = noticeEnd.getMonth() + 1;
    return `${minute} ${hour} ${day} ${month} *`;
  }

  return React.createElement('div', { className: 'notice-form section' },
    React.createElement('h2', null, 'Get Reminder When Notice Is Nearing End'),
    React.createElement('input', {
      type: 'email',
      placeholder: 'Enter your email',
      value: email,
      onChange: e => setEmail(e.target.value),
      className: 'email-input'
    }),
    React.createElement('div', { className: 'chip-group' },
      dayOptions.map(days =>
        React.createElement('button', {
          key: days,
          onClick: () => setSelectedDays(days),
          className: `chip ${selectedDays === days ? 'active' : ''}`
        }, `${days} days`)
      )
    ),
    React.createElement('button', { onClick: handleSubmit, className: 'submit-button' }, 'Send Me Reminder'),
    message && React.createElement('p', { className: 'message' }, message)
  );
}

ReactDOM.render(React.createElement(NoticeForm), document.getElementById('notice-period-root'));
</script>

<style>
.notice-form {
  max-width: 500px;
  margin: 2rem auto;
  padding: 1rem;
  background: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
  text-align: center;
}
.notice-form h2 {
  font-size: 1.25rem;
  margin-bottom: 1rem;
}
.email-input {
  padding: 0.5rem;
  width: 100%;
  margin-bottom: 1rem;
  border-radius: 4px;
  border: 1px solid #ccc;
}
.chip-group {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}
.chip {
  padding: 0.5rem 1rem;
  border-radius: 20px;
  background: #eee;
  border: none;
  cursor: pointer;
}
.chip.active {
  background-color: #007acc;
  color: white;
}
.submit-button {
  background-color: #007acc;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.message {
  margin-top: 1rem;
  font-size: 0.9rem;
  color: #c00;
}
@media (max-width: 600px) {
  .notice-form {
    padding: 0.5rem;
  }
  .chip {
    padding: 0.4rem 0.8rem;
    font-size: 0.85rem;
  }
}
</style>
