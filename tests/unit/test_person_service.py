import pytest
import mock

from src.person_service import PersonService


@pytest.mark.describe('Person Service Tests:')
class TestPersonService:

    def setup(self) -> None:
        self.person_service = PersonService()

    @mock.patch('src.person_service.pandas')
    def test_should_read_person_csv(self, mock_pandas: mock.MagicMock) -> None:
        mock_person_df = mock.MagicMock()

        mock_pandas.read_csv.return_value = mock_person_df

        response = self.person_service._read_person_csv()

        mock_pandas.read_csv.assert_called_once_with('./person.csv')

        assert mock_person_df == response

    @mock.patch('src.person_service.Person')
    @mock.patch('src.person_service.PersonService._read_person_csv')
    def test_should_create_one_person_list_with_csv_file(self,
                                                         mock_read_person_csv: mock.MagicMock,
                                                         mock_person: mock.MagicMock) -> None:
        rows = [(0, {'NAME': 'Test Name', 'AGE': 10})]

        mock_person_df = mock.MagicMock()
        mock_person_object = mock.MagicMock()

        mock_read_person_csv.return_value = mock_person_df

        mock_person_df.iterrows.return_value = rows
        mock_person.return_value = mock_person_object

        response = self.person_service.get_person_by_csv_file()

        mock_person.assert_called_once_with(name='Test Name', age=10)

        assert [mock_person_object] == response

    @mock.patch('src.person_service.Person')
    @mock.patch('src.person_service.PersonService._read_person_csv')
    def test_should_create_multiple_person_list_with_csv_file(self,
                                                              mock_read_person_csv: mock.MagicMock,
                                                              mock_person: mock.MagicMock) -> None:
        rows = [
            (0, {'NAME': 'Test Name', 'AGE': 10}),
            (1, {'NAME': 'Test Name 2', 'AGE': 12})
        ]

        mock_person_df = mock.MagicMock()
        mock_person_object = mock.MagicMock()

        mock_read_person_csv.return_value = mock_person_df

        mock_person_df.iterrows.return_value = rows
        mock_person.side_effect = [mock_person_object, mock_person_object]

        response = self.person_service.get_person_by_csv_file()

        mock_person.assert_has_calls([
            mock.call(name='Test Name', age=10),
            mock.call(name='Test Name 2', age=12)
        ])

        assert [mock_person_object, mock_person_object] == response

    @mock.patch('src.person_service.Person')
    @mock.patch('src.person_service.PersonService._read_person_csv')
    def test_should_raise_exception(self,
                                    mock_read_person_csv: mock.MagicMock,
                                    mock_person: mock.MagicMock) -> None:
        mock_read_person_csv.side_effect = Exception('Error')

        with pytest.raises(Exception):
            self.person_service.get_person_by_csv_file()

            mock_read_person_csv.assert_called_once_with()
            mock_person.assert_not_called()
