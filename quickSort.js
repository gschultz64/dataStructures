// QUICK SORT

const quickSort = arr => {
  // base case
  if (arr.length === 0) {
    return arr;
  }
  var pivot = arr[0];
  var mid = [];
  var left = [];
  var right = [];

  //  iterate over arr
  for (i = 0; i < arr.length; i++) {
    if (arr[i] > pivot) {
      right.push(arr[i])
    } else if (arr[i] < pivot) {
      left.push(arr[i])
    } else if (arr[i] == pivot) {
      mid.push(arr[i])
    }
  }
  //   return sorted items     
  return quickSort(left).concat(mid, quickSort(right));
}


data = [5, 10, 3, 90, 95, 654, 24, 9112, -6, 80];
quickSort(data);