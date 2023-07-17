// Prefilled log of hours slept per day of the week
const getSleepHours = day => {
  switch (day) {
    case 'Monday':
      return 8;
    case 'Tuesday':
      return 6;
    case 'Wednesday':
      return 8;
    case 'Thursday':
      return 10;
    case 'Friday':
      return 4;
    case 'Saturday':
      return 7;
    case 'Sunday':
      return 4;
    default: 
      console.log('Invalid day');
  }
}

//Test
//console.log(getSleepHours('Tuesday'));

// Calculates total hours of sleep in the week
const getActualSleepHours = () => getSleepHours('Monday') + getSleepHours('Tuesday') + getSleepHours('Wednesday') + getSleepHours('Thursday') + getSleepHours('Friday') + getSleepHours('Saturday') + getSleepHours('Sunday');  

console.log('Total hours slept: ' + getActualSleepHours());

// Ideal Hours per week calculated from given ideal hours per night
const getIdealSleepHours = () => {
  const idealHours = 7;
  return idealHours * 7;
};

console.log('Ideal hours of sleep per week: ' + getIdealSleepHours());

//Final calculation of hours vs hours needed/wanted
const calculateSleepDebt = () => {
  var actualSleepHours = getActualSleepHours();
  var idealSleepHours = getIdealSleepHours();
  if (actualSleepHours === idealSleepHours) {
    console.log('Well done. You have slept the perfect amount this week!');
  } else if (actualSleepHours > idealSleepHours) {
    console.log('Not bad. You slept more than you needed to by ' + (actualSleepHours - idealSleepHours) + ' hours!');
  } else if (actualSleepHours < idealSleepHours) {
    console.log('Not good! You were behind on ' + (idealSleepHours - actualSleepHours) + ' hours of sleep this week.');
  }
}

//Final run
calculateSleepDebt();
