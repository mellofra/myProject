<?php
  class Computer
  {
    public $processor;
    public $hd;
    public $cooler;
    public $placamae;
    public $gabinete;
    public $monitor;
    public $message;
     
    function processor()
    {
      $this->processor = true;
    }
    
    function hd()
    {
      $this->hd = true;
    }
    
    function cooler()
    {
      $this->cooler = true;
    }
    
    function placamae()
    {
      $this->placamae = true;
    }
    
    function gabinete()
    {
      $this->gabinete = true;
    }
    
    function monitor()
    {
      $this->monitor = true;
    }
    
    function components_verify()
    {
     if($this->processor == true)
     {
       echo "<h1>PROCESSOR: ON</h1>";
     } 
     else
     {
       echo "<h1 id='off'>PROCESSOR: OFF</h1>";
     }
      
     if($this->hd == true)
     {
       echo "<h1>HD: ON</h1>";
     } 
     else
     {
       echo "<h1 id='off'>HD: OFF</h1>";
     }
      
     if($this->cooler == true)
     {
       echo "<h1>COOLER: ON</h1>";
     } 
     else
     {
       echo "<h1 id='off'>COOLER: OFF</h1>";
     }
      
     if($this->placamae == true)
     {
       echo "<h1>MOTHER_BOARD: ON</h1>";
     } 
     else
     {
       echo "<h1 id='off'>MOTHER_BOARD: OFF</h1>";
     }
      
     if($this->monitor == true)
     {
       echo "<h1>MONITOR: ON</h1>";
     } 
     else
     {
       echo "<h1 id='off'>MONITOR: OFF</h1>";
     }
      
     if($this->gabinete == true)
     {
       echo "<h1>CABINET: ON</h1>";
     } 
     else
     {
       echo "<h1 id='off'>CABINET: OFF</h1>";
     }
    }
  }
?>