// Below is an object which stores players in a team as well as the games played in the season so far.
// Contains getter methods and functions for adding players or games as the season progresses.

const team = {
  _players: [ 
    {firstName: 'Pete', lastName: 'Wheeler', age: 23},
    {firstName: 'Katrina', lastName: 'Alvarez', age: 25},
    {firstName: 'Nia', lastName: 'Holmes', age: 20}
  ],

  _games: [
    {opponent: 'Jets', teamPoints: 42, opponentPoints: 27},
    {opponent: 'Giants', teamPoints: 45, opponentPoints: 12},
    {opponent: 'Eagles', teamPoints: 31, opponentPoints: 35}
  ],

  get players() {
    return this._players;
  },

  get games() {
    return this._games;
  },

  addPlayer(newFirstName, newLastName, newAge) {
    let player = {
      firstName: newFirstName,
      lastName: newLastName,
      age: newAge
    }
    this._players.push(player);
  },
  addGame(newOpponent, newTeamPoints, newOpponentPoints) {
    let game = {
      opponent: newOpponent,
      teamPoints: newTeamPoints,
      opponentPoints: newOpponentPoints
    }
    this._games.push(game);
  }
};

team.addPlayer('Bugs', 'Bunny', 76);
console.log(team._players);

team.addGame('Titans', 100, 98);
console.log(team._games);
