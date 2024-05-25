import './Posts.css';
import PageWrapper from './PageWrapper';
import Button from '../Button/Button';
import AddPostForm from "../Forms/AddPostForm";
import { useSelector, useDispatch } from 'react-redux';

export default function Posts(props) {

    const addPostMenuState = useSelector((state) => state.addPostMenuState);
    const dispatch = useDispatch();

    const buttonTitle = addPostMenuState? 'Закрыть форму' : 'Добавить пост';

    return (
        <PageWrapper
            pageName={'Рекламные посты'}
            controlElement={<Button name={buttonTitle} action={() => dispatch({ type: 'CASE_POST_MENUSTATE', value: !addPostMenuState })}/>}
            content={
                <div className="Posts">
                    <AddPostForm data={props.data}/>
                </div>
            }
        />
    );
}
