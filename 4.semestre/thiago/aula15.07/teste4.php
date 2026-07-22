<?php

    $a=10;
    $b=20;

    $res1= $b > $a; //true 1
    $res2= $a != $b; //true 1

    $res3= $a==$b; // false 0

    $teste= !$res3;

    echo '<br> RES1: '.$res1;
    echo '<br> RES2: '.$res2;
    echo '<br> RES3: '.$res3; //nada
    echo gettype($res1); //bool
    echo '<br> TESTE: ' .$teste; //true



?>
