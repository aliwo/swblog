pragma solidity ^0.4.15;

interface Regulator {
    function checkValue(uint amount) returns (bool);
    function loan() returns (bool);
}

contract Bank  is Regulator{
    uint private value;
    address private owner; // contract 의 소유자 = owner

    modifier ownerFunc { // ownerFunc 모디파이어는 owner 만 사용할 수 있는 함수라는 것을 나타낸다.
        require(owner == msg.sender);
        _;
    }

    function Bank (uint amount) {
        value = amount;
        owner = msg.sender;
    }

    function deposit(uint amount) {
        value += amount;
    }

    function withdraw(uint amount) {
        value -= amount;
    }

    function balance() returns (uint) {
        return value;
    }

    function checkValue(uint amount) returns (bool) {
        return amount <= value;
    }

    function loan() returns (bool) {
        return true;
    }
}

contract MyFirstContract is Bank(10) {
    string private name;
    uint private age;

    function setAge(uint newAge) {
        age = newAge;
    }

    function getAge() returns (uint) {
        return age;
    }

    function checkValue(uint amount) returns (bool) {
        return true;
    }

    function loan() returns (bool) {
        return true;
    }


}

contract TestThrows {
    function testAssert() {
        assert(1 == 2);
    }

    function testRequire() {
        require(2 == 1);
    }

    function testRevert() {
        revert();
    }

    function testThrow() {
        throw;
    }

}

// library.sol
pragma solidity ^0.4.15;

contract Libraries {
    function test() {

    }
}

// testLibrary.sol
pragma solidity ^0.4.15;

import "browser/library.sol"; // remix ide 에서 CWD 가 browser 입니다.
// import 로 libraries 를 가져옵니다.
import "github.com/aliwo/solidity/library.sol";

contract UserLibraries is Libraries {

}



