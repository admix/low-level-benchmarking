/* Low level performance benchmarking using iojs */

function SieveRegularArray(maxNum) {
    var i;
    var j;

    var Data = new Array();
    Data.length = maxNum + 1;
    for (i=2; i<=maxNum; i++) {
        Data[i] = true;
    }

    for (i=2; i<=maxNum; i++) {
        if (Data[i]) {
            for (j=i+i; j<=maxNum; j+=i) {
                Data[j] = false;
            }
        }
    }
}


function SieveBuffer(maxNum) {
    var i;
    var j;

    var Data = new Buffer(maxNum + 1);
    Data.fill(1);

    for (i=2; i<=maxNum; i++) {
	if (Data[i]) {
            for (j=i+i; j<=maxNum; j+=i) {
		Data[j] = 0;
            }
        }
    }
}



function SieveTypedArray(maxNum) {
    var i;
    var j;

    var Data = new Uint8Array(maxNum + 1);
    for (i=2; i<=maxNum; i++) {
        Data[i] = 1;
    }

    for (i=2; i<=maxNum; i++) {
        if (Data[i]) {
            for (j=i+i; j<=maxNum; j+=i) {
                Data[j] = 0;
            }
        }
    }
}

console.time("reg");
SieveRegularArray(1000000);
console.timeEnd("reg");
console.time("buffer");
SieveBuffer(1000000);
console.timeEnd("buffer");
console.time("typed");
SieveTypedArray(1000000)
console.timeEnd("typed");