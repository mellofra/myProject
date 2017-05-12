<!doctype html>
<html lang="utf-8">
  <head>
    <meta charset="utf-8"/>
  </head>
  
  <body>
    <?php
      require_once("Class.php");
    
      $c1 = new Computer;
      $c1->processor();
      $c1->hd();
      $c1->cooler();
      $c1->placamae();
      $c1->gabinete();
      $c1->monitor();
      $c1->message();
      $c1->components_verify();
    
      print_r($c1);
    ?>
  </body>
</html>