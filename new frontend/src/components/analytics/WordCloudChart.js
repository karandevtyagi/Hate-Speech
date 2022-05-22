import WordCloud from "react-d3-cloud";


const fontSize = (word) => word.value / 20;
const rotate = (word) => (word.value % 90) - 45;

export default function WordCloudChart({
  words
}) {
  const newData = words.map((item) => ({
    text: item,
    value: Math.random() * 1000
  }));
  return (
    <WordCloud
      width={1350}
      height={760}
      data={newData}
      fontSize={fontSize}
      rotate={rotate}
      padding={2}
    />
  );
}