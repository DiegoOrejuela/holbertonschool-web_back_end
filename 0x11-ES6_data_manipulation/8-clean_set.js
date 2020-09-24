export default function cleanSet(set, startString) {
  if (!startString || !startString.length) return '';
  return Array.from(set).map(
    (element) => (element.startsWith(startString) ? element.substring(startString.length) : ''),
  ).filter(Boolean).join('-');
}
