// BUCKET SORT WITH INSERTION SORT

const insertionSort = arr => {
  var i;
  var j;
  for (let i = 1; i < arr.length; i++) {
    j = i;
    while (j > 0 && arr[j - 1] > arr[j]) {
      // swap A[j] and A[j - 1]
      var x = arr[j];
      arr[j] = arr[j - 1];
      arr[j - 1] = x;
    } // end while  
  } // end for
  return arr;
}

var grades = ['A', 'A', 'C', 'D', 'F', 'B', 'B', 'A', 'F']

function bucketSortGrades(grades) {
  var buckets = {}
  // Loop through the array
  grades.forEach(grade => {
    // Look at the current letter... 
    // See if we already have a bucket for this letter
    if (buckets[grade]) {
      // if the grade already has a bucket...
      // increment the value at that bucket
      buckets[grade] += 1;
    } else {
      // the bucket doesn't exist yet
      buckets[grade] = 1
    }
  });
  // return buckets
  return buckets;
}

console.log(bucketSortGrades(grades));

function bucketSort(arr, bucketCount = 6) {
  var min = Math.min(...arr);
  var buckets = [];

  // build the buckets and distribute array elements into them
  arr.forEach(num => {
    var newIndex = Math.floor((num - min) / bucketCount);
    buckets[newIndex] = buckets[newIndex] || [];
    buckets[newIndex].push(num);
  });
  // put the elements back into the array
  var idx = 0;
  for (let i = 0; i < buckets.length; i++) {
    if (typeof buckets[i] !== 'undefined') {
      // Sort the non-empty buckets
      insertionSort(buckets[i]);
      for (let j = 0; j < buckets[i].length; j++) {
        arr[idx] = buckets[i][j]
        idx++;
      }
    }
  }
  return arr;
}

var data = [9, 18, 1, 103, -4, 13, 67, 903, 9001];

bucketSort(data);