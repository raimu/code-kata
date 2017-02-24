function fizzbuzz(input) {
  result = "";
  if (input % 3 == 0)
    result += "fizz";
  if (input % 5 == 0)
    result += "buzz";
  return result == "" ? input.toString() : result;
}