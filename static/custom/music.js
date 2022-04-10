function calculateTotalValue(length) {
  var minutes = Math.floor(length / 60),
    seconds_int = length - minutes * 60,
    seconds_str = seconds_int.toString(),
    seconds = seconds_str.substr(0, 2),
    time = minutes + ":" + seconds;

  return time;
}

function calculateCurrentValue(currentTime) {
  var current_hour = parseInt(currentTime / 3600) % 24,
    current_minute = parseInt(currentTime / 60) % 60,
    current_seconds_long = currentTime % 60,
    current_seconds = current_seconds_long.toFixed(),
    current_time =
      (current_minute < 10 ? "0" + current_minute : current_minute) +
      ":" +
      (current_seconds < 10 ? "0" + current_seconds : current_seconds);

  return current_time;
}
var prevcurrentime = 0;
var currentPlaying = null;
function togglePlay(parentElement) {
  let audio = document.getElementById(
    parentElement.parentNode.id
  ).firstElementChild;
  var playbtn = parentElement;
  console.log(playbtn);
  let tog = audio.paused === true ? true : false;
  if (tog) {
    if (currentPlaying) {
      currentPlaying.pause();
      console.log(
        "plbt",
        currentPlaying.parentNode
          .querySelector(".playbtn")
          .classList.remove("pause")
      );
    }
    playbtn.classList.add("pause");
    audio.play();
    currentPlaying = audio;
  } else {
    playbtn.classList.remove("pause");
    audio.pause();
  }
}

// var volumebar = document.getElementById("volumebar");
// //   volumebar.value = audio.volume;
// volumebar.addEventListener("click", changeVolumeBar);

// function changeVolumeBar(event) {
//   console.log(event);
//   let percent = event.offsetX / this.offsetWidth;
//   console.log(percent);
//   audio.volume = percent;
//   volumebar.value = percent / 100;
// }
function initProgressBar(element) {
  var audio = element;
  var parent = element.parentNode;
  var progressbar = parent.querySelector(`#progressbar${parent.id}`);
  var start_time = parent.querySelector("#start_time");
  var end_time = parent.querySelector("#end_time");
  var rem = parent.querySelector("#rem_time");

  var current_time = audio.currentTime;
  var length = audio.duration;
  var totalLength = "0" + calculateTotalValue(length);
  end_time.innerHTML = totalLength;
  var currentTime = calculateCurrentValue(current_time);
  start_time.innerHTML = currentTime;

  if (currentTime > prevcurrentime) {
    var rem_time = length - current_time;
    rem.innerHTML = calculateCurrentValue(rem_time);
  }
  prevcurrentime = currentTime;
  progressbar.value = audio.currentTime / audio.duration;
  progressbar.addEventListener("click", seek);
  function seek(evt) {
    var percent = evt.offsetX / this.offsetWidth;
    audio.currentTime = percent * length;
    progressbar.value = percent / 100;
  }
}

// function initPlayers(num) {
//   // pass num in if there are multiple audio players e.g 'player' + i

//   for (var i = 0; i < num; i++) {
//     (function () {
//       // Variables
//       // ----------------------------------------------------------
//       // audio embed object
//       var playerContainer = document.getElementById("player-container"),
//         player = document.getElementById("player"),
//         isPlaying = false,
//         playBtn = document.getElementById("play-btn");

//       // Controls Listeners
//       // ----------------------------------------------------------
//       if (playBtn != null) {
//         playBtn.addEventListener("click", function () {
//           togglePlay();
//         });
//       }

//       // Controls & Sounds Methods
//       // ----------------------------------------------------------
//       function togglePlay(parentElement) {
//         console.log("Parent", parentElement.parentNode.id);
//         if (player.paused === false) {
//           player.pause();
//           isPlaying = false;
//           $("#play-btn").removeClass("pause");
//         } else {
//           player.play();
//           $("#play-btn").addClass("pause");
//           isPlaying = true;
//         }
//       }
//     });
//   }
// }

// initPlayers(jQuery("#player-container").length);
