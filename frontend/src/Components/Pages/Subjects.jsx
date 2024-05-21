import './Subjects.css';
import PageWrapper from './PageWrapper';
import Card from '../Card/Card';
import Button from '../Button/Button';
import AddSubjectForm from '../Forms/AddSubjectForm';
import getImageByText from '../../api/images/image.api';

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
                        request={getImageByText}
                        params={elem.name}
                        />
                      )}
                </div>
            }
        />
    );
}
