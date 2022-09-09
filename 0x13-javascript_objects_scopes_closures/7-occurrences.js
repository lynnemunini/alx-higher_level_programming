#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
	var count = 0;
	list.forEach((v) => (v === searchElement && count++));
	return count;
}
