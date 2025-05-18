# 🎧 Moodify – Music Based on Your Mood

Moodify is a web-based music recommendation app that helps you match your mood with the perfect music genre. Select your mood from a dropdown menu and instantly discover 50 songs from Spotify that align with how you're feeling. You can also enjoy a 30-second preview of each track — all powered by the Spotify Web API.

## 🌟 Features

- 🎭 **Mood-Based Music**: Choose from a range of moods like happy, sad, energetic, relaxed, etc.
- 🎵 **Spotify Integration**: Uses the Spotify Developer API (Client ID & Secret) to fetch real-time track recommendations.
- ⏱️ **30-Second Preview**: Each song comes with a playable audio snippet.
- 💻 **Responsive UI**: Smooth animations and aesthetic design for an engaging user experience.

## 🖼️ Live Preview Animation (Moodify Mascot)

```html
<!-- Music Boy Mascot (Moodify Preview Animation) -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Music Boy</title>
  <style>
    body {
      background-color: #000;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .container {
      position: relative;
      width: 240px;
      height: 300px;
      animation: grooveScale 1.8s infinite ease-in-out;
    }
    .head {
      width: 150px;
      height: 150px;
      background: #222;
      border-radius: 50%;
      position: absolute;
      top: 60px;
      left: 45px;
      animation: bounce 2s infinite ease-in-out;
    }
    .ear {
      width: 25px;
      height: 50px;
      background: #1DB954;
      border-radius: 12px;
      position: absolute;
      top: 100px;
    }
    .ear.left { left: 20px; }
    .ear.right { right: 20px; }
    .headphones {
      width: 180px;
      height: 180px;
      border: 6px solid #1DB954;
      border-top: none;
      border-radius: 90px 90px 0 0;
      position: absolute;
      top: 30px;
      left: 30px;
    }
    .wave {
      position: absolute;
      bottom: 10px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      gap: 6px;
    }
    .bar {
      width: 8px;
      height: 25px;
      background-color: #1DB954;
      animation: sound 1s infinite ease-in-out;
    }
    .bar:nth-child(2) { animation-delay: 0.2s; }
    .bar:nth-child(3) { animation-delay: 0.4s; }
    .bar:nth-child(4) { animation-delay: 0.6s; }
    .bar:nth-child(5) { animation-delay: 0.8s; }
    @keyframes bounce {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(6px); }
    }
    @keyframes sound {
      0%, 100% { height: 25px; }
      50% { height: 40px; }
    }
    @keyframes grooveScale {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.08); }
    }
    .soundwave {
      position: absolute;
      top: 105px;
      display: flex;
      flex-direction: column;
      gap: 5px;
    }
    .soundwave.left {
      left: 0;
      align-items: flex-end;
    }
    .soundwave.right {
      right: 0;
      align-items: flex-start;
    }
    .wave-line {
      width: 20px;
      height: 4px;
      background: #1DB954;
      border-radius: 2px;
      animation: waveMove 1.2s infinite ease-in-out;
    }
    .soundwave.left .wave-line {
      animation-name: waveMoveLeft;
    }
    .soundwave.right .wave-line {
      animation-name: waveMoveRight;
    }
    .wave-line:nth-child(2) {
      width: 14px;
      animation-delay: 0.2s;
    }
    .wave-line:nth-child(3) {
      width: 8px;
      animation-delay: 0.4s;
    }
    @keyframes waveMoveLeft {
      0%, 100% { transform: translateX(0); opacity: 1; }
      50% { transform: translateX(7px); opacity: 0.6; }
    }
    @keyframes waveMoveRight {
      0%, 100% { transform: translateX(0); opacity: 1; }
      50% { transform: translateX(-7px); opacity: 0.6; }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="headphones"></div>
    <div class="ear left"></div>
    <div class="ear right"></div>
    <div class="head"></div>
    <div class="soundwave left">
      <div class="wave-line"></div>
      <div class="wave-line"></div>
      <div class="wave-line"></div>
    </div>
    <div class="soundwave right">
      <div class="wave-line"></div>
      <div class="wave-line"></div>
      <div class="wave-line"></div>
    </div>
    <div class="wave">
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
    </div>
  </div>
</body>
</html>
