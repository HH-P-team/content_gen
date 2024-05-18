import './Subjects.css';
import Card from '../Card/Card';

export default function Subjects(props) {
    return (
        <div>
            <h2>Категории продуктов</h2>
            <div className="Subjects">
                {props.data.map((elem) => <Card name={elem.name} key={elem.id}/>)}
            </div>
        </div>
    );
}
