export default function cleanSet(set, startString) {
  const startStringSanitizite = startString || false;
  return Array.from(set).map(
    (element) => (element.startsWith(startStringSanitizite) ? element.substring(startStringSanitizite.length) : ''),
  ).filter(Boolean).join('-');
}
