class RockPaperScissor extends React.Component{
  
  constructor(props){
    super(props);
    this.state = {player1: "" , player2: "",winner: ""};
    this.handleClick = this.handleClick.bind(this);
    this.decideWinner = this.decideWinner.bind(this);
    this.reset = this.reset.bind(this);
  }
  
  reset(){
    this.setState(
    {
      player1: "",
      player2: "",
      winner: ""
    }
    );
  }
  
  handleClick(props){
    this.setState(
    {
      player1: props     
    }
    );
  }
  
  player2(){
    var myArray = [
      "Rock",
      "Paper",
      "Scissor"
    ];
    var randomItem = myArray[Math.floor(Math.random()*myArray.length)];
    this.setState(
    {
      'player2':randomItem
    }
    )
  }
  
  decideWinner(){
    
    
    if (this.state.player1 === 'Rock' && this.state.player2 === 'Scissor'){
     this.setState(
     {
       winner: 'Player1'
     }
     );
    }
    
    else if (this.state.player1 === 'Scissor' && this.state.player2 === 'Paper'){
     this.setState(
     {
       winner: 'Player1'
     }
     );
    }
    
     else if (this.state.player1 === 'Paper' && this.state.player2 === 'Rock'){
     this.setState(
     {
       winner: 'Player1'
     }
     );
    }
    else if (this.state.player1 === this.state.player2 ){
     this.setState(
     {
       winner: 'Draw!'
     }
     );
    }
    else {
     this.setState(
     {
       winner: 'Player2'
     }
     );
    }
    
    
  }
 
  
  render(){
    return (
    <>
        <h1>Player1 Select:</h1>
        <button onClick={()=>this.handleClick('Rock')} >Rock</button>
        
        <button onClick={()=>this.handleClick('Paper')}>Paper</button> 
        
        <button onClick={()=>this.handleClick('Scissor')}>Scissor</button> 
        <br></br>
        <br></br>
        <button onClick={
            ()=>this.player2()}>Player2!</button>
        <br></br>
        <br></br>
        <h1>Player1: {this.state.player1}</h1>
        <h1>Player2: {this.state.player2}</h1>
        
        <button onClick={
            ()=>this.decideWinner()}>Confirm!</button>
        
        <h1>Winner: {this.state.winner}</h1>
        
        <button onClick={
            ()=>this.reset()}>Reset!</button>      
   </>
    );
  }  
}

ReactDOM.render(
<RockPaperScissor/>, document.getElementById('root')
);
