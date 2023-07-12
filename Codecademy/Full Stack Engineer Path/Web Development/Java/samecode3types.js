//Here’s how our registration works. There are adult runners (over 18 years of age) and youth runners (under 18 years of age). They can register early or late. Runners are assigned a race number and start time based on their age and registration.

// Race number:
// Early adults receive a race number at or above 1000.
// All others receive a number below 1000.

// Start time:
// Adult registrants run at 9:30 am or 11:00 am.
// Early adults run at 9:30 am.
// Late adults run at 11:00 am.
// Youth registrants run at 12:30 pm (regardless of registration).

let raceNumber = Math.floor(Math.random() * 1000);

const isEarly = true;

let runnerAge = 19;

if (runnerAge >= 18 && isEarly === true) {
  raceNumber += 1000;
  console.log(`Your race time is 9.30 and your race number is ${raceNumber}`);
} else if (runnerAge >= 18 && isEarly !== true) {
  console.log(`Your race time is 11.00 and your race number is ${raceNumber}`);
} else {
  console.log(`Your race time is 12.30 and your race number is ${raceNumber}`)
}

// Alternate code using ternery operator

const raceTime1 = runnerAge >= 18 && isEarly === true ? "9.30" : (runnerAge >= 18 && isEarly !== true ? "11.00" : "12.30");

raceNumber += runnerAge >= 18 && isEarly === true ? 1000 : 0;

console.log(`Your race time is ${raceTime1} and your race number is ${raceNumber}`);

// Alternate code using switch
let raceTime2;

switch (true) {
  case runnerAge >= 18 && isEarly === true:
    raceTime2 = "9.30";
    raceNumber += 1000;
    break;
  case runnerAge >= 18 && isEarly !== true:
    raceTime2 = "11.00";
    break;
  default:
    raceTime2 = "12.30";
    break;
}

console.log(`Your race time is ${raceTime2} and your race number is ${raceNumber}`);
