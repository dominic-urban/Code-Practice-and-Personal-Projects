console.log('Welcome to Rock Paper Scissors. Get ready to be rekt.');

// Player choice

const getUserChoice = (userInput) => {
  userInput = userInput.toLowerCase();
  if (userInput === 'rock' || userInput === 'scissors' || userInput === 'paper') {
    return userInput;
  } else {
    console.log('Error: Invalid Input.');
  }
};

// Computer choice

const getComputerChoice = () => {
  let randomNumber = Math.floor(Math.random() * 3);
  if (randomNumber === 0) {
    return 'rock';
  } else if (randomNumber === 1) {
    return 'paper';
  } else if (randomNumber === 2) {
    return 'scissors';
  } else {
    console.log('Error: Randomizer returned: ' + randomNumber);
  }
};


// Determine Winner

function determineWinner(userChoice, computerChoice) {
  if (userChoice === computerChoice) {
    return 'It\'s a tie!';
  }
  switch (userChoice) {
    case 'rock':
      return computerChoice === 'paper' ? 'I win! Mwuhaha' : 'You win!';
    case 'paper':
      return computerChoice === 'scissors' ? 'I win! Mwuhaha' : 'You win!';
    case 'scissors':
      return computerChoice === 'rock' ? 'I win! Mwuhaha' : 'You win!';
    default:
      return 'Error: Invalid Input.';
  }
}

// Play the game
const userChoice = getUserChoice('SCISSORS');
const computerChoice = getComputerChoice();

console.log('Your choice is ' + userChoice);
console.log('My choice is ' + computerChoice);
console.log(determineWinner(userChoice, computerChoice));
