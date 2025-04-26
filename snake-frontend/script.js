let playerScore = 0;
let computerScore = 0;

// Function to play the game
function playGame(playerChoice) {
  const choices = ['snake', 'water', 'gun'];
  const computerChoice = choices[Math.floor(Math.random() * 3)];
  
  let result = '';

  // Determine the winner
  if (playerChoice === computerChoice) {
    result = `It's a draw! Both chose ${playerChoice}.`;
  } else if (
    (playerChoice === 'snake' && computerChoice === 'water') ||
    (playerChoice === 'water' && computerChoice === 'gun') ||
    (playerChoice === 'gun' && computerChoice === 'snake')
  ) {
    result = `You win! ${playerChoice} beats ${computerChoice}.`;
    playerScore++;
  } else {
    result = `You lost! ${computerChoice} beats ${playerChoice}.`;
    computerScore++;
  }

  // Update the result and score
  document.getElementById('result').innerText = result;
  document.getElementById('score').innerText = `Score: Player - ${playerScore} | Computer - ${computerScore}`;
}
