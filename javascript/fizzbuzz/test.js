describe("fizzbuzz", function() {

  it("should return '1', when input is 1", function() {
    var result = fizzbuzz(1);
    expect(result).toEqual("1");
  });

  it("should return '2', when input is 2", function() {
    var result = fizzbuzz(2);
    expect(result).toEqual("2");
  });

  it("should return 'fizz', when input is 3", function() {
    var result = fizzbuzz(3);
    expect(result).toEqual("fizz")
  });

  it("should return 'buzz', when input is 5", function() {
    var result = fizzbuzz(5);
    expect(result).toEqual("buzz")
  });

  it("should return 'fizz', when input is divisible by 3", function() {
    var result = fizzbuzz(6);
    expect(result).toEqual("fizz")
  });

  it("should return 'buzz', when input is divisible by 5", function() {
    var result = fizzbuzz(10);
    expect(result).toEqual("buzz")
  });

  it("should return 'fizzbuzz', when input is divisible by 3 and 5", function() {
    var result = fizzbuzz(15);
    expect(result).toEqual("fizzbuzz")
  });

});