const cleanSet = (set, startString) => {
  let result = '';

  set.forEach((value) => {
    if (value.startsWith(startString)) {
      result += value.slice(startString.length) + '-'; // eslint-disable-line no-param-reassign
    }
  });
  return result.slice(0, -1);
};

export default cleanSet;
