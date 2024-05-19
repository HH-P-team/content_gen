import './Subjects.css';
import PageWrapper from './PageWrapper';
import Card from '../Card/Card';
import Button from '../Button/Button';

export default function Subjects(props) {
    return (
        <PageWrapper
            pageName={'Категории продуктов'}
            controlElement={<Button name={'Добавить'} action={() => console.log('trololo')}/>}
            content={
                <div className="Subjects">
                    {props.data.map((elem) => <Card name={elem.name} key={elem.id} id={elem.id}/>)}
                </div>
            }
        />
    );
}
