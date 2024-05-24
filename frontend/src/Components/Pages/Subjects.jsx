import './Subjects.css';
import PageWrapper from './PageWrapper';
import Card from '../Card/Card';
import AddSubjectForm from '../Forms/AddSubjectForm';

export default function Subjects(props) {
    return (
        <PageWrapper
            pageName={'Категории продуктов'}
            controlElement={<AddSubjectForm />}
            content={
                <div className="Subjects">
                    {props.data.map(
                      (elem) => <Card 
                        name={elem.name} 
                        key={elem.id} 
                        id={elem.id} 
                        img={elem.image}
                        />
                      )}
                </div>
            }
        />
    );
}
