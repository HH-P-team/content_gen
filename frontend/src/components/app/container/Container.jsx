import './Container.css';
import Card from '../../card/Card';

export default function Container(props) {
    return (
        <div>
            <h2>Категории продуктов</h2>
            <div className="App-container">
                {props.data.map((elem) => <Card name={elem.name} key={elem.id} />)}
            </div>
        </div>
    );
}
