import './PageWrapper.css';
import PageHeader from './PageHeader';

export default function PageWrapper(props) {
    return (
        <div className="PageWrapper">
            <PageHeader 
              pageName={props.pageName}
              controlElement={props.controlElement}
              />
            {props.content}
        </div>
    );
}
