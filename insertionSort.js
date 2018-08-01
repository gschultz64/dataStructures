const insert = (array) => {
  var i;
  var j;
  for (let i = 1; i < array.length; i++) {
    j = i;
    while (j > 0 && array[j - 1] > array[j]) {
      // swap array[j] and array[j - 1]
      var x = array[j];
      array[j] = array[j - 1];
      array[j - 1] = x;
    } // end while  
  } // end for
  return array;
}

insert([4, 1, 3, 9, 7])
