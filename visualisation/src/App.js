import 'bootstrap/dist/css/bootstrap.css';
import { LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';
const data = [{name: 'Page A', uv: 400, pv: 2400, amt: 2400}, {name: 'Page A', uv: 300, pv: 2400, amt: 2400}, {name: 'Page A', uv: 150, pv: 2400, amt: 2400}, {name: 'Page A', uv: 180, pv: 2400, amt: 2400}, {name: 'Page A', uv: 100, pv: 2400, amt: 2400}, {name: 'Page A', uv: 5, pv: 2400, amt: 2400}];

function App() {
  return (
    <div>
	<LineChart width={600} height={300} data={data}>
		<Line type="monotone" dataKey="uv" stroke="#8884d8" />
		<CartesianGrid stroke="#ccc" />
		<XAxis dataKey="name" />
		<YAxis />
	</LineChart>
    </div>
  );
}

export default App;